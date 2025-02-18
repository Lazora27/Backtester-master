import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_TTMSqueezeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und TTMSqueezeIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'TTMSqueezeIndicator': 1.0
        })
    )
