import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
