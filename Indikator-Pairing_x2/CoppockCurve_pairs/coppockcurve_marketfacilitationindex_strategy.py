import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
