import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
