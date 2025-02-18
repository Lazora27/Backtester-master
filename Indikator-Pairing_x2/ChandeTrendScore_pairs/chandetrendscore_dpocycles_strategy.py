import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'DPOCycles': 1.0
        })
    )
