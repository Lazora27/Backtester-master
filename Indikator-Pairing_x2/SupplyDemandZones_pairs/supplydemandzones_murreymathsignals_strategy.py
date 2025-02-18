import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
