import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
