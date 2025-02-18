import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'TrendCycles': 1.0
        })
    )
