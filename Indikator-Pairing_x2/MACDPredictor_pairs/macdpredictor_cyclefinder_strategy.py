import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'CycleFinder': 1.0
        })
    )
