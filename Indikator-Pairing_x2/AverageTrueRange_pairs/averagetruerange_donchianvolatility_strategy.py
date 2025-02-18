import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'DonchianVolatility': 1.0
        })
    )
