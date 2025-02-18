import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
