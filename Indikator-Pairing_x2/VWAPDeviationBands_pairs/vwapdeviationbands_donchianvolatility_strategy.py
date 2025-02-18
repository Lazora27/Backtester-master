import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'DonchianVolatility': 1.0
        })
    )
