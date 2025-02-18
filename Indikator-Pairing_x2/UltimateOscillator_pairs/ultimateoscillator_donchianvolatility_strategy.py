import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'DonchianVolatility': 1.0
        })
    )
