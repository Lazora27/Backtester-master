import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
