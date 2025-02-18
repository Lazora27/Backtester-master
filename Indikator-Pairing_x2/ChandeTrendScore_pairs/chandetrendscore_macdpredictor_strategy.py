import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MACDPredictor': 1.0
        })
    )
