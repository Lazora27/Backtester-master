import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'CyberCycle': 1.0
        })
    )
