import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'FisherSignals': 1.0
        })
    )
