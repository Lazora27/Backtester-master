import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
