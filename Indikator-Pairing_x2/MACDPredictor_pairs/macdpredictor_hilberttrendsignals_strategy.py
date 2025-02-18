import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
