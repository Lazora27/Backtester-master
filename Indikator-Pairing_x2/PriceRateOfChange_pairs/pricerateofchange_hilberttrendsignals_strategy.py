import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
