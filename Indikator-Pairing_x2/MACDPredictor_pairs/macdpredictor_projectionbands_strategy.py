import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ProjectionBands': 1.0
        })
    )
