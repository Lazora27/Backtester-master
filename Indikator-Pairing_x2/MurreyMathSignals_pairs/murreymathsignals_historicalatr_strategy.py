import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HistoricalATR': 1.0
        })
    )
