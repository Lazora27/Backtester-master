import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
