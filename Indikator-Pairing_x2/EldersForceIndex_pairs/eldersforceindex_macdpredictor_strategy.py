import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MACDPredictor': 1.0
        })
    )
