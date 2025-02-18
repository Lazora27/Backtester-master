import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
