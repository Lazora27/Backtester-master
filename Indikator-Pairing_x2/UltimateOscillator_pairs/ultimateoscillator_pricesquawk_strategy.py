import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
