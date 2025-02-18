import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
