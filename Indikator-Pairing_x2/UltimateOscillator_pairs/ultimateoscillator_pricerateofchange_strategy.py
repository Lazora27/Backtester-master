import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
