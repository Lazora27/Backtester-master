import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'IchimokuCloud': 1.0
        })
    )
