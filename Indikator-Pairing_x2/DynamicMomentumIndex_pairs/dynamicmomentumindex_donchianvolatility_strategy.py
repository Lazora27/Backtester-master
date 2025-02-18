import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
