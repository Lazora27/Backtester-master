import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
