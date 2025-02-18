import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MassIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MassIndex': 1.0
        })
    )
