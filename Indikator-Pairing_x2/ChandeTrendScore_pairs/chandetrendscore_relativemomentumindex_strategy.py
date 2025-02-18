import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
