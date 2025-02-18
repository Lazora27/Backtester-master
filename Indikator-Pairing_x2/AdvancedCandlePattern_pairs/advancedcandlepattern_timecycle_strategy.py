import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'TimeCycle': 1.0
        })
    )
