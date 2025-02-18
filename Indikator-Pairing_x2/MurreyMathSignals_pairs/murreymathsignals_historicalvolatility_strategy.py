import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
