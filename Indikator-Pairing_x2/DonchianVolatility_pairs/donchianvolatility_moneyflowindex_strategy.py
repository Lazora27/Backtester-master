import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
