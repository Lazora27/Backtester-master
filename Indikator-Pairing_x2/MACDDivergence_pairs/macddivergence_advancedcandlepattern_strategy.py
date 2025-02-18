import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
