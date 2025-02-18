import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
