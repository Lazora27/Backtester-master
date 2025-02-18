import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'FlowOfFunds': 1.0
        })
    )
