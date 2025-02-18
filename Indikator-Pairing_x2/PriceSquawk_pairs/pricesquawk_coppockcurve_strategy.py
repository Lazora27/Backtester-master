import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'CoppockCurve': 1.0
        })
    )
