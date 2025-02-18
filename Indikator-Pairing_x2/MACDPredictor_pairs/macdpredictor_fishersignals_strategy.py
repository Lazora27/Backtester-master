import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'FisherSignals': 1.0
        })
    )
