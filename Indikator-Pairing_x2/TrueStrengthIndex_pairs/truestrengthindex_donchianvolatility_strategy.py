import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
