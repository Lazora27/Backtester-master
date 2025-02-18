import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
