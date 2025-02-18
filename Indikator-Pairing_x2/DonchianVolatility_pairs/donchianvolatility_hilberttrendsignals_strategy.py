import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
