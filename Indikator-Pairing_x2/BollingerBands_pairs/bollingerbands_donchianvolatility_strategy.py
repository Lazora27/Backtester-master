import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'DonchianVolatility': 1.0
        })
    )
