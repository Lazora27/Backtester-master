import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
