import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
