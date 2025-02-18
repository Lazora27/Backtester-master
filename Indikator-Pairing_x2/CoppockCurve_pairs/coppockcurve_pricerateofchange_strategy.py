import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
