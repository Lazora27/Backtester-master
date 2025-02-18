import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_WilliamsAccumulationDistribution_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und WilliamsAccumulationDistribution
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'WilliamsAccumulationDistribution': 1.0
        })
    )
