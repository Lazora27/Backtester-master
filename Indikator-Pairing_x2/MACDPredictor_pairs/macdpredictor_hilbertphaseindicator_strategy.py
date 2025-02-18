import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HilbertPhaseIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HilbertPhaseIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HilbertPhaseIndicator': 1.0
        })
    )
