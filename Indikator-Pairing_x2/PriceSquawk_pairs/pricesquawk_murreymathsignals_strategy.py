import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
