import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
