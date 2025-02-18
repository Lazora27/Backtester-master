import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'TrendCycles': 1.0
        })
    )
