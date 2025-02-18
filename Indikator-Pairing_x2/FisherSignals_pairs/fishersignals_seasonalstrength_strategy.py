import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'SeasonalStrength': 1.0
        })
    )
