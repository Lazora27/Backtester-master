import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
